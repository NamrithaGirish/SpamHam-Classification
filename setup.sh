mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableeCORS = false\n\
\n\
" > ~/.streamlit/config.toml
