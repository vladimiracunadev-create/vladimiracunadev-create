#!/usr/bin/env python3
"""Paso 2 de 3 — detecta cada tecnología del Stack en cada repositorio.

Lee .cache/stack_evidence/ (paso 1) y aplica reglas por tecnología: lenguajes
según GitHub, dependencias en manifiestos, workflows, Docker/Compose, archivos
de infraestructura, carpetas o archivos dedicados y README. Escribe el resultado
en docs/data/stack_evidence.json: para cada tecnología, los repositorios donde
aparece, el tipo de evidencia y un archivo de muestra.

Las reglas están en este archivo (R): cada tecnología puede tener varias
(lang, file, dep, wf, dock, iac, path, readme). Una tecnología sin regla o sin
resultado queda como «declarada por el autor».
"""
import glob
import json
import os
import re

ROOT =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
E = os.path.join(ROOT, ".cache", "stack_evidence")
data = json.load(open(os.path.join(ROOT, "scripts", "stack_data.json"), encoding="utf-8"))
ITEMS = data["items"]
U_PROFILE = "vladimiracunadev-create"
# Los servicios de AWS solo se buscan en repositorios de AWS o que dependen de un SDK de AWS:
# palabras como «lambda» aparecen en cursos sin relación con AWS Lambda.
AWS_REPOS = {"aws-desktop-studio", "proyectos-aws", "proyectos-aws-gitlab", "multi-cloud-engineering-program"}
AWS_DEP = r"(?i)(?<![\w.\-@/])(boto3|aws-sdk|@aws-sdk/[\w\-]+|aws-cdk|aws-cdk-lib)(?![\w\-])"

def dw(*names):  # nombre de dependencia suelto (no parte de otro nombre)
    return r"(?i)(?<![\w.\-@/])(?:" + "|".join(names) + r")(?![\w\-])"
def ci(p): return "(?i)" + p

# regla: lang, file(path de manifiesto), dep (texto de manifiestos), wf, dock, iac, path (árbol), readme, any (texto de cualquier archivo recogido), todos
R = {}
def rule(name, **k): R[name] = k
# --- lenguajes ---
for n, l in {"Python": ["Python"], "JavaScript": ["JavaScript"], "TypeScript": ["TypeScript"], "Rust": ["Rust"], "Go": ["Go"], "Java": ["Java"], "PHP": ["PHP"], "C#": ["C#"], "Dart": ["Dart"],
             "Kotlin": ["Kotlin"], "Swift": ["Swift"], "Ruby": ["Ruby"], "Elixir": ["Elixir"], "Zig": ["Zig"], "Clojure": ["Clojure"], "C": ["C"], "Solidity": ["Solidity"], "Bash": ["Shell"],
             "PowerShell": ["PowerShell"], "HTML": ["HTML"], "CSS": ["CSS"], "Erlang": ["Erlang"], "F#": ["F#"], "Crystal": ["Crystal"], "GDScript": ["GDScript"], "HCL": ["HCL"]}.items():
    rule(n, lang=l)
rule("WebAssembly", path=r"\.wasm$|(^|/)pkg/.*\.wasm", dep=dw("wasm-bindgen", "wasm-pack", "wasm32"))
rule("SQL", lang=["PLpgSQL", "TSQL", "PLSQL", "SQL"], path=r"\.sql$")
# --- frameworks ---
rule("Node.js", file=r"(^|/)package\.json$")
for n, d in {"Express": ["express"], "React": ["react"], "Vue": ["vue", "@vue/[\\w\\-]+", "nuxt"], "Svelte": ["svelte", "@sveltejs/[\\w\\-]+"], "Astro": ["astro"], "Vite": ["vite"], "Vitest": ["vitest"],
             "FastAPI": ["fastapi"], "Flask": ["flask"], "Django": ["django"], "Tauri": ["tauri", "@tauri-apps/[\\w\\-]+"], "Electron": ["electron"], "Capacitor": ["@capacitor/[\\w\\-]+"],
             "PyTorch": ["torch"], "scikit-learn": ["scikit-learn", "sklearn"], "Polars": ["polars"], "pandas": ["pandas"], "NumPy": ["numpy"], "Optuna": ["optuna"], "SHAP": ["shap"],
             "Transformers": ["transformers"], "PEFT / LoRA": ["peft"], "Playwright": ["playwright", "@playwright/test"], "pytest": ["pytest"], "Streamlit": ["streamlit"], "Pydantic": ["pydantic"],
             "Tokio": ["tokio"], "Axum": ["axum"], "SQLx": ["sqlx"], "Serde": ["serde", "serde_json"]}.items():
    rule(n, dep=dw(*d), **({"path": r"(^|/)%s/" % n.lower()} if n in ("Vue","Svelte","Astro") else {}))
rule("Spring Boot", dep=r"(?i)spring-boot|org\.springframework\.boot")
rule("ASP.NET / .NET", file=r"\.(csproj|fsproj)$", dep=r"Microsoft\.AspNetCore")
rule("Laravel", dep=r"laravel/framework")
rule("Rails", dep=r"(?im)^\s*gem\s+['\"]rails['\"]")
rule("Flutter", dep=r"(?m)^\s*flutter:\s*$|sdk:\s*flutter")
rule("Qt / PySide6", dep=dw("PySide6", "PyQt5", "PyQt6"))
rule("Godot", path=r"(^|/)project\.godot$")
rule("Jupyter", path=r"\.ipynb$", dep=dw("jupyter", "notebook", "ipykernel", "jupyterlab"))
rule("gRPC", dep=dw("grpcio", "grpcio-tools", "tonic", "google\\.golang\\.org/grpc", "@grpc/[\\w\\-]+", "grpc"), path=r"\.proto$")
# --- arquitecturas (curadas desde el README + detección en árbol y README) ---
CUR = {"Local-first": ["empresa-operativa-chile", "ai-dataset-foundry"], "Event-driven (n8n)": ["social-bot-scheduler"], "Circuit breaker": ["problem-driven-systems-lab"],
       "Idempotency": ["problem-driven-systems-lab"], "Double-entry ledger": ["universal-payments-engineering-lab"], "Plugin architecture": ["agentic-plugins-toolkit"],
       "Agent graphs": ["langgraph-realworld", "operational-ai-agents"], "Domain-first": ["rhino-suite"], "Micro-apps": ["microsistemas"], "Embedded database": ["gabysql"],
       "IaC / CI-CD": ["proyectos-aws"], "Dead-letter queue": ["social-bot-scheduler"]}
rule("Local-first", readme=ci(r"local[- ]first"))
rule("Offline-first / PWA", path=r"(^|/)(sw|service-?worker)\.js$|manifest\.(web)?(json|webmanifest)$", readme=ci(r"offline[- ]first"))
rule("Event-driven (n8n)", docker=ci(r"n8nio/n8n|image:\s*n8n"), path=r"(^|/)n8n")
rule("Idempotency", readme=ci(r"idempoten"), path=ci(r"idempoten"))
rule("Circuit breaker", readme=ci(r"circuit[- _]?breaker"), path=ci(r"circuit[-_ ]?breaker"))
rule("Dead-letter queue", readme=ci(r"dead[- _]?letter|\bDLQ\b"), path=ci(r"dead[-_ ]?letter|(^|/)dlq"))
rule("Outbox", readme=ci(r"\boutbox\b"), path=ci(r"outbox"))
rule("Backpressure", readme=ci(r"back-?pressure|contrapresi"), path=ci(r"back-?pressure"))
rule("State machines", readme=ci(r"state[- _]?machine|m[aá]quinas? de estados?|\bFSM\b"), path=ci(r"state[-_ ]?machine|(^|/)fsm"))
rule("Agent graphs", dep=dw("langgraph"))
rule("Human-in-the-loop", readme=ci(r"human[- _]in[- _]the[- _]loop|\bHITL\b|humano en el bucle"), path=ci(r"human[-_]in[-_]the[-_]loop|hitl"))
rule("Plugin architecture", readme=ci(r"plugin architecture|arquitectura de plugins|registro de plugins|plugin registry"))
rule("Domain-first", readme=ci(r"domain[- ]first|dominio primero|modelo de dominio primero"))
rule("Monorepo", path=r"(^|/)(pnpm-workspace\.yaml|lerna\.json|nx\.json|turbo\.json)$", dep=r"(?m)^\[workspace\]")
rule("Micro-apps", readme=ci(r"micro-?sistemas|micro-?apps"))
rule("Embedded database", readme=ci(r"base de datos embebida|embedded database"))
rule("Read-only by default", readme=ci(r"read-only by default|solo lectura por defecto|solo lectura|read-only"))
rule("Double-entry ledger", readme=ci(r"double[- ]entry|partida doble|ledger balanceado"))
rule("ADRs", path=r"(^|/)(adr|ADR|adrs|decisions)/|(^|/)(adr|ADR)-?\d+")
rule("IaC / CI-CD", path=r"\.tf$|(^|/)\.gitlab-ci\.yml$", wf=r".")
rule("Docker-first", readme=ci(r"docker[- ]first"))
CUR["Docker-first"] = ["problem-driven-systems-lab"]
CUR["Agentic Plugins"] = ["agentic-plugins-toolkit"]
# --- bases de datos ---
rule("PostgreSQL", dock=ci(r"image:\s*['\"]?(postgres|pgvector|timescale|supabase/postgres)|FROM\s+postgres"), dep=dw("psycopg2?", "psycopg", "asyncpg", "pg", "postgres", "node-postgres", "tokio-postgres", "pgx", "lib/pq"), lang=["PLpgSQL"])
rule("MySQL", dock=ci(r"image:\s*['\"]?mysql"), dep=dw("mysql2?", "mysqlclient", "mysql-connector-python", "PyMySQL", "go-sql-driver/mysql"))
rule("MariaDB", dock=ci(r"mariadb"), dep=dw("mariadb"))
rule("SQLite", dep=dw("sqlite3", "better-sqlite3", "rusqlite", "aiosqlite", "sqlite", "mattn/go-sqlite3", "sqflite", "sqlite3_flutter_libs"), path=r"\.(sqlite3?|db3)$")
rule("MongoDB", dock=ci(r"image:\s*['\"]?mongo"), dep=dw("mongodb", "mongoose", "pymongo", "motor"))
rule("Redis", dock=ci(r"image:\s*['\"]?redis"), dep=dw("redis", "ioredis", "redis-py", "go-redis"))
rule("Neo4j", dock=ci(r"neo4j"), dep=dw("neo4j", "neo4j-driver"), lang=["Cypher"])
rule("Cassandra", dock=ci(r"cassandra"), dep=dw("cassandra-driver", "gocql"), lang=["CQL"])
rule("Elasticsearch", dock=ci(r"elasticsearch"), dep=dw("elasticsearch", "@elastic/elasticsearch"))
rule("ClickHouse", dock=ci(r"clickhouse"), dep=dw("clickhouse-driver", "clickhouse-connect", "@clickhouse/client"))
rule("CockroachDB", dock=ci(r"cockroach"), dep=ci(r"cockroach"))
rule("InfluxDB", dock=ci(r"influxdb"), dep=dw("influxdb-client", "influxdb"))
rule("TimescaleDB", dock=ci(r"timescale"), dep=ci(r"timescale"))
rule("DuckDB", dep=dw("duckdb"))
rule("SQL Server", dock=ci(r"mssql|sqlserver|sql-server"), dep=dw("mssql", "pyodbc", "tedious", "Microsoft\\.Data\\.SqlClient", "System\\.Data\\.SqlClient", "tiberius"), lang=["TSQL"])
rule("Oracle", dock=ci(r"oracle|gvenzl"), dep=dw("oracledb", "cx_Oracle", "ojdbc\\d*", "node-oracledb"))
rule("pgvector", dock=ci(r"pgvector"), dep=dw("pgvector"))
rule("PostgREST", dock=ci(r"postgrest"))
rule("GraphQL", dep=dw("graphql", "apollo-server", "@apollo/[\\w\\-]+", "graphene", "strawberry-graphql", "async-graphql", "gqlgen", "graphql-java", "gql"), path=r"\.graphql$")
rule("Hasura", dock=ci(r"hasura"), path=ci(r"hasura"))
rule("Qdrant", dep=dw("qdrant-client", "qdrant"), dock=ci(r"qdrant"))
CUR["GabySQL (Rust)"] = ["gabysql"]
rule("GabySQL (Rust)")
# --- BI ---
rule("Power BI (.pbix ×3)", path=r"\.pbix$|(^|/)powerbi/")
rule("DAX", path=r"\.dax$")
rule("Star schema", readme=ci(r"star schema|esquema en estrella"))
# --- nube / devops ---
rule("AWS", dep=dw("boto3", "aws-sdk", "@aws-sdk/[\\w\\-]+", "aws-cdk", "aws-cdk-lib", "aws-lambda-powertools", "aws-sam-cli"), iac=r"(?i)provider\s+\"aws\"|AWS::|aws_[a-z_]+\"", wf=ci(r"aws-actions|configure-aws-credentials|aws s3|aws cloudformation|aws lambda"))
rule("Azure", path=ci(r"azure"), dep=dw("azure-[\\w\\-]+", "@azure/[\\w\\-]+", "azurerm"), iac=ci(r"azurerm|provider\s+\"azure"), wf=ci(r"azure/(login|webapps|cli)|az login"))
rule("Google Cloud", path=ci(r"(^|[-_/])(gcp|google[-_ ]cloud)([-_/.]|$)"), dep=dw("google-cloud-[\\w\\-]+", "@google-cloud/[\\w\\-]+"), iac=ci(r"provider\s+\"google|google_[a-z_]+\""), wf=ci(r"google-github-actions|gcloud "))
rule("Terraform", path=r"\.tf$", wf=ci(r"setup-terraform|terraform (init|plan|apply)"))
rule("Kubernetes", path=ci(r"(^|/)(k8s|kubernetes|helm)([-_/]|$)"), iac=r"(?i)Chart\.ya?ml|kind:\s*(Deployment|StatefulSet|DaemonSet)", docker=r"(?i)kind:\s*(Deployment|StatefulSet)", wf=ci(r"kubectl|helm "))
rule("Docker / Compose", todos="docker")
rule("GitHub Actions", todos="workflow")
rule("Git", todos="all"); rule("GitHub", todos="all")
rule("GitLab", path=r"(^|/)\.gitlab-ci\.yml$", file=r"\.gitlab-ci\.yml$")
rule("Linux", docker=ci(r"FROM\s+[^\s]*(ubuntu|debian|alpine|fedora|centos|rockylinux|archlinux)"), path=r"(^|/)(linux/|[^/]+\.AppImage$|[^/]+\.deb$)")
rule("Nginx", docker=ci(r"nginx"), path=ci(r"nginx(\.conf)?"))
rule("Make", path=r"(^|/)Makefile$")
rule("Inno Setup", path=r"\.iss$")
rule("FinOps", readme=ci(r"finops"), path=ci(r"finops"))
rule("CI/CD", wf=r".", path=r"(^|/)\.gitlab-ci\.yml$")
# --- servicios AWS ---
AWSX = {"Amplify": r"amplify", "S3": r"AWS::S3::|aws_s3_|\bs3 (sync|cp)|S3Client|client-s3|s3://|(^|[-_/])s3([-_/.]|$)", "CloudFront": r"cloudfront", "Route 53": r"route-?\s?53|aws_route53", "Lambda": r"AWS::Serverless::Function|AWS::Lambda|aws_lambda_|lambda_handler|(^|[-_/])lambda([-_/.]|$)",
        "API Gateway": r"ApiGateway|aws_api_gateway|apigateway|API Gateway|api-gateway", "SAM": r"Transform:\s*AWS::Serverless|sam (build|deploy)|samconfig", "DynamoDB": r"dynamodb", "Cognito": r"cognito", "WAF": r"wafv2|aws_wafv2|AWS::WAF|(^|[-_/])waf([-_/.]|$)",
        "IAM / OIDC": r"aws_iam_|AWS::IAM::|configure-aws-credentials|AssumeRoleWithWebIdentity|(^|[-_/])oidc([-_/.]|$)", "EventBridge": r"eventbridge|aws_cloudwatch_event|AWS::Events::", "SNS": r"aws_sns_|AWS::SNS::|SNSClient|client-sns",
        "SQS": r"aws_sqs_|AWS::SQS::|SQSClient|client-sqs", "CloudWatch": r"cloudwatch", "X-Ray": r"x-?ray", "Synthetics": r"synthetics", "Bedrock": r"bedrock", "ECS Fargate": r"aws_ecs_|AWS::ECS::|fargate", "ECR": r"aws_ecr_|AWS::ECR::|\becr\b",
        "EKS": r"aws_eks_|AWS::EKS::|eksctl|client-eks|(^|[-_/])eks([-_/.]|$)|eks", "EC2": r"EC2Client|client-ec2|ec2\.|aws_instance|AWS::EC2::Instance|describe-instances|DescribeInstances|boto3\.client\(.ec2", "RDS": r"RDSClient|client-rds|aws_db_instance|AWS::RDS::|DescribeDBInstances|describe-db-instances|rds",
        "VPC": r"aws_vpc|AWS::EC2::VPC|DescribeVpcs|describe-vpcs", "Secrets Manager": r"secretsmanager|secrets-?manager|SecretsManager", "CloudFormation": r"AWS::CloudFormation|cloudformation|client-cloudformation", "Cost Explorer / Budgets": r"Cost ?Explorer|cost-explorer|GetCostAndUsage|client-cost-explorer|aws_budgets|AWS::Budgets|ce:Get|budgets?"}
for n, rx in AWSX.items(): rule(n, awsany=ci(rx))
# --- observabilidad ---
rule("Prometheus", dock=ci(r"prom/prometheus|prometheus"), path=ci(r"prometheus"), dep=dw("prometheus_client", "prom-client", "prometheus", "metrics-exporter-prometheus"))
rule("Grafana", dock=ci(r"grafana"), path=ci(r"grafana"))
rule("OpenTelemetry", dep=dw("opentelemetry[\\w\\-\\.]*", "@opentelemetry/[\\w\\-]+"), dock=ci(r"otel|opentelemetry"))
rule("Kafka", dock=ci(r"kafka|redpanda"), dep=dw("kafka-python", "confluent-kafka", "kafkajs", "rdkafka", "sarama", "kafka-clients", "aiokafka"))
rule("RabbitMQ", dock=ci(r"rabbitmq"), dep=dw("pika", "amqplib", "amqp", "lapin", "aio-pika", "bunny"))
rule("MQTT (Mosquitto)", dock=ci(r"mosquitto|emqx|mqtt"), dep=dw("paho-mqtt", "mqtt", "rumqttc", "paho"))
rule("Elasticsearch / Kibana", dock=ci(r"kibana"))
rule("cAdvisor", dock=ci(r"cadvisor"))
rule("k6", dock=ci(r"k6"), path=ci(r"(^|/)k6[-_/]|\.k6\."), wf=ci(r"k6-action|grafana/k6"))
# --- IA ---
rule("Claude Code", path=r"(^|/)(\.claude/|CLAUDE\.md$)")
rule("Claude Skills", path=r"(^|/)(\.claude/skills/|skills/[^/]+/SKILL\.md$)", readme=ci(r"claude skills?"))
rule("Codex Skills", path=r"(^|/)(AGENTS\.md|\.codex/|codex[^/]*/)", readme=ci(r"codex skills?"))
rule("Agentic Plugins", readme=ci(r"agentic plugins?"))
rule("MCP", dep=dw("mcp", "fastmcp", "@modelcontextprotocol/[\\w\\-]+", "modelcontextprotocol"), path=ci(r"(^|/)mcp[-_/]|mcp_server|mcp-server"))
rule("LangGraph", dep=dw("langgraph", "langchain", "langchain-core"))
rule("Ollama", dep=dw("ollama"), dock=ci(r"ollama"))
rule("n8n", dock=ci(r"n8nio/n8n|image:\s*n8n"), path=ci(r"(^|/)n8n"))
rule("RAG", dep=dw("faiss-cpu", "faiss", "chromadb", "qdrant-client", "llama-index", "sentence-transformers"), readme=ci(r"\bRAG\b|retrieval[- ]augmented"))
rule("Whisper", dep=dw("openai-whisper", "faster-whisper", "whisper", "whisper-rs", "whisper\\.cpp"), path=ci(r"whisper"))
# --- flujo IA / seguridad / plataformas / publicación ---
rule("ChatGPT Plus"); rule("Antigravity"); rule("OpenCode")
rule("Codex", path=r"(^|/)(AGENTS\.md|\.codex/)")
rule("VS Code", path=r"(^|/)\.vscode/")
rule("CodeQL", wf=ci(r"codeql")); rule("Semgrep", wf=ci(r"semgrep")); rule("Bandit", wf=ci(r"bandit"), dep=dw("bandit")); rule("Trivy", wf=ci(r"trivy"))
rule("Grype", wf=ci(r"grype|anchore")); rule("Gitleaks", wf=ci(r"gitleaks"), path=ci(r"gitleaks")); rule("TruffleHog", wf=ci(r"trufflehog"))
rule("SBOM CycloneDX", wf=ci(r"cyclonedx|\bsbom\b"), dep=ci(r"cyclonedx"), path=ci(r"sbom|cyclonedx"))
rule("OpenSSF Scorecard", wf=ci(r"scorecard"))
rule("Dependabot", path=r"(^|/)\.github/dependabot\.ya?ml$")
rule("Windows", path=r"\.(iss|msi|bat|ps1)$|(^|/)windows/")
rule("macOS", path=r"(^|/)macos/|\.dmg$|Info\.plist$")
rule("iOS", path=r"(^|/)ios/|\.xcodeproj/")
rule("Android", path=r"(^|/)android/|AndroidManifest\.xml$|\.apk$")
rule("Web / PWA", path=r"manifest\.(web)?(json|webmanifest)$|(^|/)(sw|service-?worker)\.js$")
rule("Cloudflare", path=ci(r"(^|/)wrangler\.toml$"), wf=ci(r"cloudflare/wrangler-action|cloudflare/pages-action"))
rule("Vercel", path=ci(r"(^|/)vercel\.json$"), wf=ci(r"vercel"), readme=ci(r"vercel\.app|desplegad[oa] en vercel|deployed on vercel|Vercel \("))
rule("GitHub Pages", wf=ci(r"deploy-pages|upload-pages-artifact|gh-pages|peaceiris/actions-gh-pages"))
rule("macOS"); R["macOS"] = dict(path=r"(^|/)macos/|\.dmg$|Info\.plist$")

def load():
    repos = {}
    for f in glob.glob(E + "/*.json"):
        d = json.load(open(f, encoding="utf-8"))
        if d["repo"] == U_PROFILE: continue  # el README del perfil no es evidencia de sí mismo
        repos[d["repo"]] = d
    return repos

def detect(repos):
    out = {}
    for block, items in enumerate(ITEMS):
        for name in items:
            k = R.get(name, {}); hits = {}
            for repo, d in repos.items():
                ev = []; samples = []
                paths = d["paths"]; files = d["files"]; langs = d.get("languages", {})
                def add(t, s=None):
                    if t not in ev: ev.append(t)
                    if s and len(samples) < 2 and s not in samples: samples.append(s)
                if k.get("lang"):
                    for l in k["lang"]:
                        if langs.get(l, 0) >= 300: add("lang", None)
                if k.get("file"):
                    for p in files:
                        if re.search(k["file"], p): add("manifest", p); break
                    else:
                        for p in paths:
                            if re.search(k["file"], p): add("manifest", p); break
                if k.get("dep"):
                    for p, (kind, t) in files.items():
                        if kind == "manifest" and re.search(k["dep"], t): add("manifest", p); break
                if k.get("wf"):
                    for p, (kind, t) in files.items():
                        if kind == "workflow" and re.search(k["wf"], t): add("workflow", p); break
                if k.get("dock"):
                    for p, (kind, t) in files.items():
                        if kind == "docker" and re.search(k["dock"], t): add("docker", p); break
                if k.get("iac"):
                    for p, (kind, t) in files.items():
                        if kind in ("iac", "manifest") and re.search(k["iac"], t): add("iac", p); break
                if k.get("path"):
                    for p in paths:
                        if re.search(k["path"], p): add("path", p); break
                if k.get("awsany") and (repo in AWS_REPOS or any(re.search(AWS_DEP, t) for kd, t in files.values() if kd == "manifest")):
                    for p, (kind, t) in files.items():
                        if kind != "extra" and re.search(k["awsany"], t): add("iac", p); break
                    else:
                        for p in paths:
                            if re.search(k["awsany"], p): add("path", p); break
                    rdm = files.get("README.md")
                    if not ev and rdm and re.search(k["awsany"], rdm[1]) and repo in ("aws-desktop-studio", "proyectos-aws", "proyectos-aws-gitlab"):
                        add("readme", "README.md")
                if k.get("todos"):
                    t = k["todos"]
                    if t == "all": add("all")
                    elif t == "docker" and any(kd == "docker" for kd, _ in files.values()): add("docker", next(p for p, (kd, _) in files.items() if kd == "docker"))
                    elif t == "workflow" and any(kd == "workflow" for kd, _ in files.values()): add("workflow", next(p for p, (kd, _) in files.items() if kd == "workflow"))
                if k.get("readme"):
                    rd = files.get("README.md")
                    if rd and re.search(k["readme"], rd[1]) and not ev: add("readme", "README.md")
                if repo in CUR.get(name, []) and not ev: add("curated", None)
                if ev:
                    w = sum({"manifest": 5, "workflow": 4, "docker": 4, "iac": 4, "lang": 3, "path": 2, "all": 1, "curated": 2, "readme": 1}[e] for e in ev)
                    hits[repo] = dict(repo=repo, ev=ev, files=samples, w=w, bytes=max([langs.get(l, 0) for l in k.get("lang", [])] or [0]), platform=d.get("platform", "github"))
            out[name] = dict(block=block, repos=sorted(hits.values(), key=lambda h: (-h["bytes"], -h["w"], h["repo"])))
    return out

def main():
    import datetime
    repos = load()
    res = detect(repos)
    meta = dict(fecha=datetime.date.today().isoformat(),
                repositorios_github=sum(1 for d in repos.values() if d.get("platform", "github") == "github"),
                repositorios_gitlab=sum(1 for d in repos.values() if d.get("platform") == "gitlab"))
    salida = dict(meta=meta, tecnologias={
        n: dict(bloque=v["block"], repos=[dict(repo=h["repo"], plataforma=h["platform"], evidencia=h["ev"], archivos=h["files"]) for h in v["repos"]])
        for n, v in res.items()})
    os.makedirs(os.path.join(ROOT, "docs", "data"), exist_ok=True)
    json.dump(salida, open(os.path.join(ROOT, "docs", "data", "stack_evidence.json"), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    sin = [n for n, v in res.items() if not v["repos"]]
    print("repositorios:", len(repos), "| tecnologías:", len(res), "| sin repositorio público:", len(sin), sin)


if __name__ == "__main__":
    main()
