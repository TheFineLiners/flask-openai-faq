from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "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"


@app.route("/generate-faq", methods=["POST"])
def generate_faq():
    data = request.json
    question = data.get("question")

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Answer briefly, friendly, and SEO optimized.",
                },
                {"role": "user", "content": question},
            ],
            max_tokens=200,
            temperature=0.7,
        )

        answer = response.choices[0].message.content.strip()
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
