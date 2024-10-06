pipeline {
    agent any

    stages {
        stage('Force Install Miniconda') {
            steps {
                sh '''
                    # Define the Miniconda installation directory
                    MINICONDA_DIR="$HOME/miniconda"

                    # Remove any existing Miniconda installation to force reinstallation
                    echo "Removing any existing Miniconda installation..."
                    rm -rf $MINICONDA_DIR

                    # Determine architecture and download the correct Miniconda installer
                    ARCH=$(uname -m)
                    if [ "$ARCH" = "x86_64" ]; then
                        CONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
                    elif [ "$ARCH" = "aarch64" ]; then
                        CONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh"
                    else
                        echo "Unsupported architecture: $ARCH"
                        exit 1
                    fi

                    # Download and install Miniconda
                    echo "Downloading Miniconda from $CONDA_URL..."
                    curl -Lo miniconda.sh $CONDA_URL
                    bash miniconda.sh -b -p $MINICONDA_DIR
                    rm miniconda.sh

                    # Verify the installation and list contents for debugging
                    if [ -f "$MINICONDA_DIR/etc/profile.d/conda.sh" ]; then
                        echo "Miniconda installed successfully."
                        ls -alh $MINICONDA_DIR/etc/profile.d/  # List the directory for debugging
                    else
                        echo "Miniconda installation failed."
                        exit 1
                    fi
                '''
            }
        }

        stage('Create Python 3.8 Environment') {
            steps {
                // Use bash to source the environment and create the Python environment
                sh '''
                    bash -c "
                    source $HOME/miniconda/etc/profile.d/conda.sh && \
                    conda create -y -n py38 python=3.8 && \
                    conda activate py38 && \
                    python --version
                    "
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                // Use bash to activate the environment and run the script
                sh '''
                    bash -c "
                    source $HOME/miniconda/etc/profile.d/conda.sh && \
                    conda activate py38 && \
                    python main.py
                    "
                '''
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }

    post {
        always {
            sh 'echo "Cleanup complete"'
        }
    }
}