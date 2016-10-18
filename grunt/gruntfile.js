module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                compress: {},
                beautify: true
      },
      build: {
        src: 'src/<%= pkg.name %>.js',
        dest: '../umairabbasi/static/js/<%= pkg.name %>.min.js'
      }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          '../umairabbasi/static/css/umairabbasi.css': 'src/umairabbasi.scss'
          //'//Volumes/autopub/iamahornet.com/global/css/main.css': 'src/main.scss',
          //'//Volumes/autopub/www.emporia.edu/global/css/main.css': 'src/main.scss'      // 'destination': 'source'
        }
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['uglify', 'sass'],
        options: {
          livereload: true
        },
      },
    }
    });

    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['uglify', 'sass', 'watch']);

};