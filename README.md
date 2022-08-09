# airflow-dags
Airflow DAGs git sync repository

### Airflow best practice

1. 원자성(atomicity)  
Task는 성공적으로 수행하여 적절한 결과를 생성하거나 시스템 상태에 영향을 미치지 않고 실패하도록 정의한다.

1. 멱등성(idempotency)  
Task는 다시 실행해도 전체 결과가 변경되지 않아야 한다.  

### Directory desc

|path|desc|etc|
|:---|:---|:---|
|/dags|DAG List||
