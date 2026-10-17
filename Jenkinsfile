pipeline {
    agent any

    stages {
        stage('Verificar Docker') {
            steps {
                sh '''
                    set -e
                    echo "Verificando Docker..."
                    docker --version
                    docker info
                '''
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh '''
                    set -e
                    docker build -t etl-pytest:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Ejecutar pruebas pytest') {
            steps {
                sh '''
                    set -e
                    mkdir -p reports

                    docker run --rm \
                        -v "${WORKSPACE}/reports:/app/reports" \
                        etl-pytest:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'reports/pytest_results.csv,reports/junit.xml',
                allowEmptyArchive: true
            )

            junit(
                testResults: 'reports/junit.xml',
                allowEmptyResults: true
            )
        }
    }
}