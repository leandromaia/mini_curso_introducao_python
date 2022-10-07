def process_tuple(data_tpl):
    for v in data_tpl:
        if type(v) == str:
            print(f"String encontrada:\n {v}")

    

if __name__ == "__main__":
    hard_data = (23, 45.5, "Hello", True, ["a", "b", "c"], "Python")
    process_tuple(hard_data)
