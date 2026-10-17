
pipeline {
    agent any

    enviroment {
        DOCKER='C:\\Users\\Patri\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {
        stage('Construir imagen Docker') {
            steps {
                bat "\"${DOCKER}\" build -t etl-pytest:${BUILD_NUMBER} .'
            }
        }

        stage('Ejecutar pruebas pytest') {
            steps {
                bat 'mkdir -p reports'

                bat '''
                    "${DOCKER}" run --rm \
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
