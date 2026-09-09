     -H "Content-Type: application/json" \
     -d '{"name": "Persistence Test Item", "description": "Verifying volume data retention"}'
   ```

3. **Tear down the containers (simulating a full server shutdown/redeployment):**
   ```bash
   docker compose down
   ```

4. **Bring the stack back up:**
   ```bash
   docker compose up -d
   ```

5. **Retrieve records from the API:**
   ```bash
   curl "http://localhost:8000/items"
   ```
   *Result:* The previously created item is successfully returned with its original ID and timestamp intact, proving that the PostgreSQL named volume successfully preserved state across container lifecycles.

---

## Stretch Goals Implemented

- **Redis Integration:** Added a Redis 7 Alpine container in `docker-compose.yml` with a corresponding connection string in `.env`.
- **SQL Optimization & EXPLAIN ANALYZE:** 
  - Added an explicit index on the items table: `CREATE INDEX idx_items_name ON items(name);`
  - Execution plans verified a transition from a costly sequential scan (`Seq Scan`) to an efficient index lookup (`Bitmap Heap Scan`).