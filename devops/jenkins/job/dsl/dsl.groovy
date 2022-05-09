job('child_job_name') {
  description('This is my awesome Job')

  parameters {
    stringParam('Planet', defaultValue = 'world', description = 'This is the world')
    booleanParam('FLAG', true)
    choiceParam('OPTION', ['option 1 (default)', 'option 2', 'option 3'])
  }

  scm {
    // disable creating a tag for each build by default
    git('https://github.com/jenkins-docs/simple-java-maven-app', 'master', { node -> node / 'extensions' << '' })
  }

  triggers {
    cron('H 5 * * 7')
  }

  steps {
    wrappers {
      colorizeOutput(colorMap = 'xterm')
    }

    // Plain shell script
    shell("""
      echo 'Hello World'
      echo 'Running a multiline shell script'
      /tmp/script.sh
    """)

    // Ansible Playbook
    ansiblePlaybook('/etc/ansible/plays/i2b-cl/some_playbook.yml') {
      inventoryPath('/etc/ansible/plays/i2b-cl/hosts')
      tags('cool')
      forks(1)
      colorizedOutput(true)
      additionalParameters('--vault-password-file $HOME/pass-vault/i2b-cl.txt')
      extraVars {
        extraVar('whoami', '${param1}', false)
        extraVar('my_pass', 'some_pass', true)
      }
    }

    // Build, test and deploy java project
    maven {
      mavenInstallation('mvn-jenkins') // maven instance config created in jenkins
      goals('-B -DskipTests clean package')
    }
    maven {
      mavenInstallation('mvn-jenkins')
      goals('test')
    }
    shell('''
      echo Deploying jar package
      java -jar $WORKSPACE/target/my-app-1.0-SNAPSHOT.jar
    ''')
  }

  publishers {
    archiveArtifacts('target/*.jar')
    archiveJunit('target/surefire-reports/*.xml')
    mailer('me@example.com', true, true)
  }
}