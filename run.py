"""Start the monitoring demo on 0.0.0.0:5777."""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Binding to 0.0.0.0 exposes the app on all interfaces — demo only.
    # Auth and agent token will be required in later phases.
    app.run(host="0.0.0.0", port=5777, debug=True)
