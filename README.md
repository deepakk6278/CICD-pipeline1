# Frontend CI/CD Project

A beginner-friendly project for Cloud Computing and DevOps Experiments 4, 5, and 6.

## Components
- Flask web application with `/`, `/health`, and `/api/student` endpoints
- Dockerfile and requirements file
- GitHub Actions CI workflow in `.github/workflows/ci.yml`
- Jenkins pipeline for tests, Docker build, and Amazon ECR push
- Kubernetes Deployment and NodePort Service manifests
- AWS Lambda handler in `lambda_function.py`

## Phase 1: Run locally (Windows PowerShell)

Prerequisites: Python 3.11+ and Git.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open these pages in your browser:
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/health
- http://127.0.0.1:5000/api/student

If PowerShell blocks virtual-environment activation, install dependencies with `python -m pip install -r requirements.txt` and run `python app.py`.

## Smoke test

```powershell
python -m pip install -r requirements.txt
python -c "from app import app; c=app.test_client(); print(c.get('/').status_code, c.get('/health').json, c.get('/api/student').json)"
```

## Docker test

```powershell
docker build -t frontend-cicd-project:local .
docker run --rm -p 5000:5000 frontend-cicd-project:local
```

## Push to the existing GitHub repository

Target repository: `https://github.com/deepakk6278/CICD-pipeline1.git`

From the project root:

```powershell
git status
git add .
git commit -m "Add CI/CD demonstration project"
git branch -M main
git remote -v
git push -u origin main
```

If `origin` points to a different repository, correct it with:

```powershell
git remote set-url origin https://github.com/deepakk6278/CICD-pipeline1.git
```

Never commit AWS credentials, GitHub tokens, passwords, `.env` files, or `.pem` keys.

## Next phases
1. Push and verify source code in GitHub.
2. Verify Docker works locally.
3. Configure Jenkins on the existing EC2 instance.
4. Create ECR repository `image-regi` in `ap-south-1` and configure the EC2 IAM role.
5. Set AWS account ID in Jenkins and run the pipeline.
6. Deploy the ECR image to Minikube, expose the Service, and scale replicas.
7. Create and test the Lambda handler in AWS.

The Jenkinsfile assumes a Linux Jenkins agent with Python 3, pip, Docker, AWS CLI, and an EC2 IAM role with ECR push permissions. Do not run it unchanged on a Windows-only Jenkins agent.
