from neo4jCrud import neo4jCrud


if __name__ == "__main__":
    app = neo4jCrud("bolt://localhost:7687", "neo4j", "maximus11")

    feature_id = 123
    feature_name = "My Feature"
    branch_name = "My Branch"

    # create
    app.add_feature(feature_id, feature_name)
    app.add_branch(branch_name)
    app.create_feature_branch_relationship(feature_id, feature_name, branch_name)

    # destroy
    app.remove_feature_branch_relationship(feature_id, branch_name)
    app.remove_feature(feature_id)
    app.remove_branch(branch_name)

    app.close()
