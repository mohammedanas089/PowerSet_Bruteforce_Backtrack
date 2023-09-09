import streamlit as st

# Function to generate powerset using brute force
def powerset_bruteforce(input_set):
    n = len(input_set)
    powerset = []

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(input_set[j])
        powerset.append(subset)

    return powerset

# Function to generate powerset using backtracking
def powerset_backtracking(input_set):
    def backtrack(start, current_set):
        powerset.append(current_set[:])

        for i in range(start, len(input_set)):
            current_set.append(input_set[i])
            backtrack(i + 1, current_set)
            current_set.pop()

    powerset = []
    backtrack(0, [])
    return powerset

# Streamlit UI
st.title("Powerset Finder App")

input_set = st.text_input("Enter a set of elements (comma-separated):")
input_set = [x.strip() for x in input_set.split(',')]

if st.button("Find Powerset - Brute Force"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_bruteforce(input_set)
        st.success(f"Powerset (Brute Force): {powerset}")

if st.button("Find Powerset - Backtracking"):
    if not input_set:
        st.warning("Please enter a set of elements.")
    else:
        powerset = powerset_backtracking(input_set)
        st.success(f"Powerset (Backtracking): {powerset}")

st.sidebar.markdown("Description: This is a Minor Assignment to Find the Powerset of given list of set by either Bruteforce or Backtracking")

