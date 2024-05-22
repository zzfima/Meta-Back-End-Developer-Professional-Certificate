from neo4j import GraphDatabase


class neo4jCrud:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_feature(self, feature_id: int, feature_name: str):
        with self.driver.session() as session:
            session.run(
                "CREATE (f:Feature {id: $featureId, name: $featureName})",
                featureId=feature_id,
                featureName=feature_name,
            )

    def add_branch(self, branch_name: str):
        with self.driver.session() as session:
            session.run(
                "CREATE (:Branch {name: $branchName})",
                branchName=branch_name,
            )

    def create_feature_branch_relationship(
        self, feature_id: int, feature_name: str, branch_name: str
    ):
        with self.driver.session() as session:
            session.run(
                "MERGE (f:Feature {id: $featureId, name: $featureName}) "
                "MERGE (b:Branch {name: $branchName}) "
                "MERGE (f)-[:MERGED_INTO]->(b)",
                featureId=feature_id,
                featureName=feature_name,
                branchName=branch_name,
            )

    def remove_feature_branch_relationship(self, feature_id: int, branch_name: str):
        with self.driver.session() as session:
            session.run(
                "MATCH (f:Feature {id: $featureId})-[r:MERGED_INTO]->(b:Branch {name: $branchName}) "
                "DELETE r",
                featureId=feature_id,
                branchName=branch_name,
            )

    def remove_branch(self, branch_name: str):
        with self.driver.session() as session:
            session.run(
                "MATCH (b:Branch {name: $branchName}) DETACH DELETE b",
                branchName=branch_name,
            )

    def remove_feature(self, feature_id: int):
        with self.driver.session() as session:
            session.run(
                "MATCH (f:Feature {id: $featureId}) DETACH DELETE f",
                featureId=feature_id,
            )
