from client import AutonomousCommerceDataOptimizerClient

def main():
    client = AutonomousCommerceDataOptimizerClient()
    res = client.optimize(raw_catalog=[{"title": "Noise Cancelling Headphones", "category": "Electronics", "price": 199.99}])
    print(f"Quality Score Improvement: +{res['quality_score_improvement']}%")
    print(f"Optimized Item Title: {res['optimized_catalog'][0]['seo_title']}")
    print(f"AEO Tags: {res['optimized_catalog'][0]['aeo_tags']}")

if __name__ == "__main__":
    main()
