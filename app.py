from flask import Flask, render_template
import pandas as pd
import markdown
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        # ----------------------------
        # Load Dataset
        # ----------------------------
        dataset_path = os.path.join("data", "2-orders-data.xlsx")
        df = pd.read_excel(dataset_path)

        # Show first 10 rows
        table = df.head(10).to_html(
            classes="table table-bordered table-striped table-hover",
            index=False
        )

    except Exception as e:
        table = f"<p style='color:red;'>Error loading dataset: {str(e)}</p>"

    try:
        # ----------------------------
        # Load README and Convert Markdown to HTML
        # ----------------------------
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()

        readme_html = markdown.markdown(
            readme_content,
            extensions=["fenced_code", "tables"]
        )

    except Exception as e:
        readme_html = f"<p style='color:red;'>Error loading README: {str(e)}</p>"

    return render_template(
        "index.html",
        table=table,
        readme=readme_html
    )


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
