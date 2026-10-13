
pipeline {
    agent any

    stages {
        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t etl-pytest:${BUILD_NUMBER} .'
            }
        }

        stage('Ejecutar pruebas pytest') {
            steps {
                sh 'mkdir -p reports'

                sh '''
                    docker run --rm \
                        -v "$WORKSPACE/reports:/app/reports" \
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
