from __future__ import annotations

import sqlite3
from typing import Any, Dict, Optional

from flask import Flask, jsonify, request


DATABASE_NAME = 'rental_db.sqlite'


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    return {k: row[k] for k in row.keys()}


def create_app() -> Flask:
    app = Flask(__name__)

    # ---------- Helpers ----------
    def get_by_id(table: str, pk_col: str, pk: Any) -> Optional[Dict[str, Any]]:
        with get_db_connection() as conn:
            cur = conn.execute(f"SELECT * FROM {table} WHERE {pk_col}=?", (pk,))
            row = cur.fetchone()
            return row_to_dict(row) if row else None

    def list_all(table: str) -> list[Dict[str, Any]]:
        with get_db_connection() as conn:
            cur = conn.execute(f"SELECT * FROM {table}")
            return [row_to_dict(r) for r in cur.fetchall()]

    def insert_row(table: str, fields: Dict[str, Any]) -> int:
        keys = ", ".join(fields.keys())
        placeholders = ", ".join(["?"] * len(fields))
        values = tuple(fields.values())
        with get_db_connection() as conn:
            cur = conn.execute(f"INSERT INTO {table} ({keys}) VALUES ({placeholders})", values)
            conn.commit()
            return cur.lastrowid

    def update_row(table: str, pk_col: str, pk: Any, fields: Dict[str, Any]) -> int:
        if not fields:
            return 0
        sets = ", ".join([f"{k}=?" for k in fields.keys()])
        values = tuple(fields.values()) + (pk,)
        with get_db_connection() as conn:
            cur = conn.execute(f"UPDATE {table} SET {sets} WHERE {pk_col}=?", values)
            conn.commit()
            return cur.rowcount

    def delete_row(table: str, pk_col: str, pk: Any) -> int:
        with get_db_connection() as conn:
            cur = conn.execute(f"DELETE FROM {table} WHERE {pk_col}=?", (pk,))
            conn.commit()
            return cur.rowcount

    # ---------- Clients ----------
    @app.get('/api/clients')
    def api_list_clients():
        return jsonify(list_all('clients'))

    @app.get('/api/clients/<int:customer_id>')
    def api_get_client(customer_id: int):
        item = get_by_id('clients', 'customer_id', customer_id)
        if not item:
            return jsonify({'error': 'Client not found'}), 404
        return jsonify(item)

    @app.post('/api/clients')
    def api_create_client():
        data = request.get_json(silent=True) or {}
        required = ['name', 'phone']
        missing = [f for f in required if not data.get(f)]
        if missing:
            return jsonify({'error': 'Missing required fields', 'fields': missing}), 400
        fields = {
            'name': data.get('name'),
            'phone': data.get('phone'),
            'email': data.get('email'),
            'country': data.get('country'),
        }
        # Remove None values for optional fields
        fields = {k: v for k, v in fields.items() if v is not None}
        new_id = insert_row('clients', fields)
        return jsonify(get_by_id('clients', 'customer_id', new_id)), 201

    @app.put('/api/clients/<int:customer_id>')
    def api_update_client(customer_id: int):
        if not get_by_id('clients', 'customer_id', customer_id):
            return jsonify({'error': 'Client not found'}), 404
        data = request.get_json(silent=True) or {}
        fields = {k: data[k] for k in ['name', 'phone', 'email', 'country'] if k in data}
        update_row('clients', 'customer_id', customer_id, fields)
        return jsonify(get_by_id('clients', 'customer_id', customer_id))

    @app.delete('/api/clients/<int:customer_id>')
    def api_delete_client(customer_id: int):
        deleted = delete_row('clients', 'customer_id', customer_id)
        if deleted == 0:
            return jsonify({'error': 'Client not found'}), 404
        return '', 204

    # ---------- Bookings ----------
    @app.get('/api/bookings')
    def api_list_bookings():
        return jsonify(list_all('bookings'))

    @app.get('/api/bookings/<int:booking_id>')
    def api_get_booking(booking_id: int):
        item = get_by_id('bookings', 'booking_id', booking_id)
        if not item:
            return jsonify({'error': 'Booking not found'}), 404
        return jsonify(item)

    @app.post('/api/bookings')
    def api_create_booking():
        data = request.get_json(silent=True) or {}
        required = ['customer_id', 'check_in', 'check_out']
        missing = [f for f in required if data.get(f) in (None, '')]
        if missing:
            return jsonify({'error': 'Missing required fields', 'fields': missing}), 400
        # optional fields
        fields = {
            'customer_id': data.get('customer_id'),
            'check_in': data.get('check_in'),
            'check_out': data.get('check_out'),
            'nights': data.get('nights'),
            'total_price': data.get('total_price'),
        }
        fields = {k: v for k, v in fields.items() if v is not None}
        new_id = insert_row('bookings', fields)
        return jsonify(get_by_id('bookings', 'booking_id', new_id)), 201

    @app.put('/api/bookings/<int:booking_id>')
    def api_update_booking(booking_id: int):
        if not get_by_id('bookings', 'booking_id', booking_id):
            return jsonify({'error': 'Booking not found'}), 404
        data = request.get_json(silent=True) or {}
        fields = {k: data[k] for k in ['customer_id', 'check_in', 'check_out', 'nights', 'total_price'] if k in data}
        update_row('bookings', 'booking_id', booking_id, fields)
        return jsonify(get_by_id('bookings', 'booking_id', booking_id))

    @app.delete('/api/bookings/<int:booking_id>')
    def api_delete_booking(booking_id: int):
        deleted = delete_row('bookings', 'booking_id', booking_id)
        if deleted == 0:
            return jsonify({'error': 'Booking not found'}), 404
        return '', 204

    # ---------- OPEX ----------
    @app.get('/api/opex')
    def api_list_opex():
        return jsonify(list_all('opex'))

    @app.get('/api/opex/<int:opex_id>')
    def api_get_opex(opex_id: int):
        item = get_by_id('opex', 'opex_id', opex_id)
        if not item:
            return jsonify({'error': 'Opex not found'}), 404
        return jsonify(item)

    @app.post('/api/opex')
    def api_create_opex():
        data = request.get_json(silent=True) or {}
        required = ['opex_date', 'category', 'amount']
        missing = [f for f in required if data.get(f) in (None, '')]
        if missing:
            return jsonify({'error': 'Missing required fields', 'fields': missing}), 400
        fields = {
            'opex_date': data.get('opex_date'),
            'category': data.get('category'),
            'amount': data.get('amount'),
            'notes': data.get('notes'),
        }
        fields = {k: v for k, v in fields.items() if v is not None}
        new_id = insert_row('opex', fields)
        return jsonify(get_by_id('opex', 'opex_id', new_id)), 201

    @app.put('/api/opex/<int:opex_id>')
    def api_update_opex(opex_id: int):
        if not get_by_id('opex', 'opex_id', opex_id):
            return jsonify({'error': 'Opex not found'}), 404
        data = request.get_json(silent=True) or {}
        fields = {k: data[k] for k in ['opex_date', 'category', 'amount', 'notes'] if k in data}
        update_row('opex', 'opex_id', opex_id, fields)
        return jsonify(get_by_id('opex', 'opex_id', opex_id))

    @app.delete('/api/opex/<int:opex_id>')
    def api_delete_opex(opex_id: int):
        deleted = delete_row('opex', 'opex_id', opex_id)
        if deleted == 0:
            return jsonify({'error': 'Opex not found'}), 404
        return '', 204

    # ---------- CAPEX ----------
    @app.get('/api/capex')
    def api_list_capex():
        return jsonify(list_all('capex'))

    @app.get('/api/capex/<int:capex_id>')
    def api_get_capex(capex_id: int):
        item = get_by_id('capex', 'capex_id', capex_id)
        if not item:
            return jsonify({'error': 'Capex not found'}), 404
        return jsonify(item)

    @app.post('/api/capex')
    def api_create_capex():
        data = request.get_json(silent=True) or {}
        required = ['capex_date', 'category', 'amount']
        missing = [f for f in required if data.get(f) in (None, '')]
        if missing:
            return jsonify({'error': 'Missing required fields', 'fields': missing}), 400
        fields = {
            'capex_date': data.get('capex_date'),
            'category': data.get('category'),
            'amount': data.get('amount'),
            'notes': data.get('notes'),
            'is_depreciable': data.get('is_depreciable'),
        }
        fields = {k: v for k, v in fields.items() if v is not None}
        new_id = insert_row('capex', fields)
        return jsonify(get_by_id('capex', 'capex_id', new_id)), 201

    @app.put('/api/capex/<int:capex_id>')
    def api_update_capex(capex_id: int):
        if not get_by_id('capex', 'capex_id', capex_id):
            return jsonify({'error': 'Capex not found'}), 404
        data = request.get_json(silent=True) or {}
        fields = {k: data[k] for k in ['capex_date', 'category', 'amount', 'notes', 'is_depreciable'] if k in data}
        update_row('capex', 'capex_id', capex_id, fields)
        return jsonify(get_by_id('capex', 'capex_id', capex_id))

    @app.delete('/api/capex/<int:capex_id>')
    def api_delete_capex(capex_id: int):
        deleted = delete_row('capex', 'capex_id', capex_id)
        if deleted == 0:
            return jsonify({'error': 'Capex not found'}), 404
        return '', 204

    # Health check
    @app.get('/health')
    def health():
        return jsonify({'status': 'ok'})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)
