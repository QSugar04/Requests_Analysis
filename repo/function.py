import ast
import matplotlib.pyplot as plt
import os

def count_functions_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

# 使用 ast 模块解析文件内容为抽象语法树
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Error parsing {file_path}: {e}")
        return 0

# 遍历 AST 节点，统计 ast.FunctionDef 类型的节点数量
    function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
    return function_count

#分析指定目录及其子目录中的所有 Python 文件，并统计每个文件中的函数数量
def analyze_requestss_directory(requestss_directory):
    function_counts = []

    for root, dirs, files in os.walk(requestss_directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                functions = count_functions_in_file(file_path)
                function_counts.append(functions)

    return function_counts

#绘制函数数量分布的直方图
def plot_histogram(function_counts):
    plt.hist(function_counts, bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Number of Functions in requestss Files')
    plt.xlabel('Number of Functions')
    plt.ylabel('Number of Files')
    plt.savefig("Distribution of Number of Functions in requestss Files.png")
    plt.close()



# 指定仓库路径
requestss_directory = "C:\\Users\ASUS\\requests"

# 分析requests仓库中的函数数量
function_counts = analyze_requestss_directory(requestss_directory)

# 输出结果
print(f"Total number of functions in requestss repository: {sum(function_counts)}")
print(f"Average number of functions per file: {sum(function_counts) / len(function_counts)}")

plot_histogram(function_counts)


