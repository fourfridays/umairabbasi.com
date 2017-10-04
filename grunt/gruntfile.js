module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['src/jquery-2.2.4.js', 'node_modules/bootstrap-sass/assets/javascripts/bootstrap/transition.js', 'node_modules/bootstrap-sass/assets/javascripts/bootstrap/collapse.js', 'src/umairabbasi.js'],
                dest: 'dist/js/umairabbasi.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                compress: {},
                beautify: true
        },
        dist: {
            files: {
                '/mnt/volume-nyc1-01-part1/static/js/umairabbasi.min.js': ['<%= concat.dist.dest %>'],
               //'../static/js/umairabbasi.min.js': ['<%= concat.dist.dest %>'],
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          '/mnt/volume-nyc1-01-part1/static/css/umairabbasi.css': 'src/umairabbasi.scss'
          //'../static/css/umairabbasi.css': 'src/umairabbasi.scss'
        }
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['concat', 'uglify', 'sass'],
        options: {
          livereload: true
        },
      },
    }
    });

    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.
loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'watch']);

};
