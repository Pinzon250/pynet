from libs.db.drivers.sqlserver import SQLServerClient

def get_database(driver: str, config: dict):
    driver = driver.lower()
    
    if driver == "sqlserver":
        return SQLServerClient(config)
    # Futuros drivers
    # elif driver == "postgresql":
    #     return PostgresClient(config)
    else:
        raise ValueError(f"Motor de base de datos no soportado {driver}")