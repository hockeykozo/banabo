base_dir = "/home/takashi/dev/banabo"
tool_dir = "#{base_dir}/scripts"
python_dir = "#{tool_dir}/python"
sh_dir = "#{tool_dir}/sh"

module.exports = (robot) ->
    robot.respond /help/i, (msg) ->
        @exec = require('child_process').exec
        command = "cat #{base_dir}/help"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    robot.respond /dig (.*)/i, (msg) ->
        @exec = require('child_process').exec
        command = "bash #{sh_dir}/test.sh #{msg.match[1]}"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?
            
    robot.respond /weather (.*)|weather/,(msg) ->
        @exec = require('child_process').exec
        if "#{msg.match[1]}" == "undefined"
            date = 0
        else
            date = "#{msg.match[1]}"
        command = "python #{python_dir}/weather.py #{date}"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    robot.hear /さわちゃん|さーわちゃん/,(msg) ->
        @exec = require('child_process').exec
        command = "python #{python_dir}/random_comments.py sawabo"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    robot.respond /kotaro/,(msg) ->
        @exec = require('child_process').exec
        command = "python #{python_dir}/random_comments.py kotaro"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?
