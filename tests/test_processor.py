import processor
import os
import pytest

TESTFILE_PATH = 'tests/test_file'

class TestWriteIntegers:
    def setup_class(self):
        self.filepath = TESTFILE_PATH
        processor.write_integers(self.filepath)

    def test_file_exists(self):
        assert os.path.exists(self.filepath) == True
    
    def test_file_contents(self):
        with open(self.filepath, 'r') as f:
            lines = f.readlines()
        assert lines == [f'{i}\n' for i in range(101)]

    def teardown_class(self):
        os.remove(self.filepath)

class TestGetIntegers:
    def test_nonexistent_file(self):
        with pytest.raises(IOError):
            processor.get_integers('nonexistent_file')
    
    def test_not_a_file(self):
        with pytest.raises(IOError):
            processor.get_integers('tests')
    
    def test_file_sanity_test(self):
        self.malformed_file_path = 'tests/malformed_file'
        with open(self.malformed_file_path, 'w') as f:
            f.write('banana')
        with pytest.raises(Exception):
            processor.get_integers(self.malformed_file_path)
        os.remove(self.malformed_file_path)
    
    def test_get_integers(self):
        processor.write_integers(TESTFILE_PATH)
        assert processor.get_integers(TESTFILE_PATH) == [i for i in range(50)]
        os.remove(TESTFILE_PATH)