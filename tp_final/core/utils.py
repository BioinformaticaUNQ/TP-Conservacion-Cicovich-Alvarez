import os

__repo_path__ = os.path.join(os.getcwd(), "repository")

def getRepositoryPath():
	if not os.path.exists(__repo_path__):
		os.makedirs(__repo_path__)
	return __repo_path__

def getRepositoryFilePath(file):
	return os.path.join(getRepositoryPath(), file)

if __name__ == '__main__':
    print(getRepositoryFilePath('test.txt'))