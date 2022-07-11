import feast



fs = feast.FeatureStore(repo_path = "/feature_repo")
features = fs.get_feature_view(name = "driver_hourly_stats_view").features
for i in features:
    print(i.name)