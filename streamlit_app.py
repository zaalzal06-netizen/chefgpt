import streamlit as st
from openai import OpenAI

# 🔑 Your OpenAI API key
client = OpenAI(api_key="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")

st.set_page_config(page_title="ChefGPT 🍳", page_icon="🍽")
st.title("🍽 ChefGPT - Recipe Assistant")
st.write("Apne ingredients likhein aur ChefGPT aapke liye recipe banayega!")

ingredients = st.text_area("Ingredients (comma separated, e.g., chicken, tomato, rice)")

if st.button("Generate Recipe 🍳"):
    if ingredients.strip() == "":
        st.warning("Please enter some ingredients!")
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[{"role": "user", "content": f"Please give me a recipe using these ingredients: {ingredients}"}]
            )
            recipe = response.choices[0].message["content"]
            st.success("✅ Recipe Ready!")
            st.write(recipe)
        except Exception as e:
            st.error(f"Error: {e}")
