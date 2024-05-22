from neo4j import GraphDatabase


class Neo4jApp:
    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_feature_branch_relationship(self, feature_id: int, branch_name: str):
        with self.driver.session() as session:
            session.run(
                "MATCH (f:Feature {id: $featureId}), (b:Branch {name: $branchName}) "
                "MERGE (f)-[:MERGED_INTO]->(b)",
                featureId=feature_id,
                branchName=branch_name,
            )

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


if __name__ == "__main__":
    app = Neo4jApp("bolt://localhost:7687", "neo4j", "maximus11")

    feature_id = 123  # Replace with your actual feature ID
    feature_name = "My Feature"  # Replace with your actual feature name
    branch_name = "My Branch"  # Replace with your actual branch name
    app.create_feature_branch_relationship(feature_id, feature_name, branch_name)

    # branch_name = "My Branch"  # Replace with your actual branch name
    # app.add_branch(branch_name)

    # feature_id = 123  # Replace with your actual feature ID
    # feature_name = "My Feature"  # Replace with your actual feature name
    # app.add_feature(feature_id, feature_name)

    # feature_id = 123  # Replace with your actual feature ID
    # branch_name = "my_branch"  # Replace with your actual branch name
    # app.create_feature_branch_relationship(feature_id, branch_name)

    app.close()
