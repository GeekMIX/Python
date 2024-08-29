# test_remove_file.py

import os
from pathlib import Path
import pytest
from remove_file import remove_file  # 假设函数位于remove_file模块中

# 测试文件存在时删除文件的功能
def test_remove_existing_file(tmp_path: Path):
    # 创建一个临时文件
    file = tmp_path / "test_file.txt"
    file.touch()
    # 确保文件存在
    assert file.exists()
    # 调用待测函数，尝试删除文件
    remove_file(str(file))
    # 确认文件被删除
    assert not file.exists()

# 测试文件不存在时的处理
def test_remove_nonexistent_file():
    # 提供一个不存在的文件路径
    nonexistent_file = "/path/to/nonexistent/file.txt"
    # 由于文件不存在，调用待测函数不应抛出异常
    try:
        remove_file(nonexistent_file)
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

# 如果需要，可以添加更多的测试用例来覆盖不同的边界条件和可能的异常情况。

test_remove_nonexistent_file()