# main.py
import text_utils as tu

def main():
    sample_text = "hello world"

    reversed_text = tu.reverse_string(sample_text)
    capitalized_text = tu.capitalize_string(sample_text)

    print(f"Original text: {sample_text}")
    print(f"Reversed text: {reversed_text}")
    print(f"Capitalized text: {capitalized_text}")

if __name__ == "__main__":
    main()
