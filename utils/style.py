def readStyles(file_path) -> str:
    try:
        with open(f"styles/{file_path}", "r") as style:
            return style.read()
    except Exception as e:
        raise e
