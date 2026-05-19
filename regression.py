import kagglehub

# Download latest version
path = kagglehub.competition_download('sofia-ml-regression-2026-spring')

print("Path to competition files:", path)