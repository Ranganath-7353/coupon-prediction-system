import pandas as pd

df = pd.read_csv("/Users/ranganath/Desktop/Predicting Coupon Acceptance/data/cleaned/cleaned_coupon_data.csv")

coupon_acceptance = (
    df.groupby("coupon")["Accept(Y/N?)"]
    .agg(
        total_customers="count",
        accepted="sum"
    )
)

coupon_acceptance["acceptance_rate"] = (
    coupon_acceptance["accepted"]
    / coupon_acceptance["total_customers"]
    * 100
)

coupon_acceptance = coupon_acceptance.sort_values(
    "acceptance_rate",
    ascending=False
)

print(coupon_acceptance)