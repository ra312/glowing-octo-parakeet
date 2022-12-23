"""About page shown when the user enters the application"""
import streamlit as st


def write():
    """Used to write the about page in the app.py file"""
    st.title("Dr. Rauan Akylzhanov")
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    st.markdown(
        """
**Software Engineer/Machine Learning Systems **

[[**Email**](mailto:akylzhanov.r@gmail.com)
""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """Experience
----------

**Competera Pricing Platform, 2021-present:**

Software Engineer/Machine Learning Platform
- implemented and deployed scalable automated Vertex pipelines to train neural networks on large datasets
- reduced infrastructure costs 10 times by migrating kubeflow pipelines to Vertex AI
- developed (blueprint) and prototyped federated learning (PyTorch) approach to scale training and reduce time to train on marketplace datasets
- productionized a transformer model (TensorFlow) on Vertex AI, designed and automated performance metrics calculation (human-in-the-loop) via google.cloud.aiplatform

**Kcell , 2020-2021:**

Software Engineer/Machine Learning Platform

building a scalable, distributed, analytical engine (Hadoop Data Platform, k8s)
- designed and productionized reliable ML kubeflow pipelines to regularly run and monitor python ML models deployed and configured Airflow production cluster (Red Hat servers) to migrate kubeflow ETLs
- developed and deployed custom ETL pipelines (Airflow) to ingest data into Hadoop cluster
- developed Airflow DAGs to regularly calculate user app activity metrics (spark aggregates)
- support k8s platform by adding more nodes, configuring NVIDIA driver, resource allocation
- automated Hortonworks Data Platform deployment via ansible-playbooks

**Macquarie Group Limited , 2019-2020:**
machine learning engineering for the low-laten
cy intraday trading platform: ETLs, end-to-end automated ML development

**Research Associate, Imperial College, London, 2017-2019**

taught introductory courses on Data Science topics:
- High Performance Computing (M3C)
- Data Science, introduction to R programming (M3A50)
- Introduction to Regression and Statistical Computing (STAT 410)

**Tech Skills**
- Python, SQL: Pandas, NumPy, cx-Oracle, Feast, PySpark, papermill, pypiserver
- DBMS: Oracle, PostgreSQL
- ML: TensorFlow, SciKit-Learn, PyTorch, XGBoost, LightGBM, SparkMLLib, HyperOpt
- Cluster&Infra: Docker, Kubernetes, Kubeflow, GCP,Vertex AI, Airflow, Spark, Hadoop, Hive, Flink, Kafka, Presto, Ambari, Ansible
- Other CentOS(yum, systemd, NFS), git, Jira, Confluence

**Education**

- 2014-2018 [PhD](phd) in Mathematics, Imperial College, London
- [Doris Chen Merit Award](award) for exceptional research
- 2007-2012 Specialist in Computer Science, Moscow State University, Moscow, With Honours computer systems architecture, object-oriented-programming, computationall statistics, high-performance distributed computing
- 2014-2017 Imperial College Data Science Society and Machine Learning Society training in essential Data Science topics, platform for interaction between Imperial College and industry, hackathons

""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    write()
