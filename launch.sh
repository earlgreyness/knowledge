FOLDER="$HOME/repos/expenses"

xfce4-terminal --geometry=173x39 \
      -T "Expenses | Flask" \
      --working-directory="$FOLDER" \
      -e "bash -c 'python3 app.py; exec bash'" \
--tab -T "Expenses | Angular" \
      --working-directory="$FOLDER/frontend" \
      -e "bash -c 'ng serve; exec bash'"
