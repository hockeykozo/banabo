# Const
base_dir = "/home/takashi/dev/banabo"
tool_dir = "#{base_dir}/scripts"
python_dir = "#{tool_dir}/python"
sh_dir = "#{tool_dir}/sh"

## Var 
#cron = require('cron').CronJob

# Functions
module.exports = (robot) ->
#    new cron '0 0 20 * * *', () =>
#        command_weather = "python #{python_dir}/weather.py 0"
#        command_news = "python #{python_dir}/news.py"
#        @exec = require('child_process').exec
#        @exec command_weather, (error, stdout, stderr) ->
#            msg.send error if error?
#            msg.send stdout if stdout?
#            msg.send stderr if stderr?
#        @exec command_news, (error, stdout, stderr) ->
#            msg.send error if error?
#            msg.send stdout if stdout?
#            msg.send stderr if stderr?
#

    # Banabo Help
    robot.respond /help/i, (msg) ->
        @exec = require('child_process').exec
        command = "cat #{base_dir}/help"
        exec_cmd command
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    # Dig 
    robot.respond /dig (.*)/i, (msg) ->
        @exec = require('child_process').exec
        command = "bash #{sh_dir}/test.sh #{msg.match[1]}"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?
            
    # Banabo Weather 
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

    # Sawa-chan 
    robot.hear /さわちゃん|さーわちゃん/,(msg) ->
        @exec = require('child_process').exec
        command = "python #{python_dir}/random_comments.py sawabo"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    # Kotaro 
    robot.respond /kotaro/,(msg) ->
        @exec = require('child_process').exec
        command = "python #{python_dir}/random_comments.py kotaro"
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    # Memo
    robot.respond /memo (.*)/i, (msg) ->
        user_name = msg.message.user.name
        option = "#{msg.match[1]}"
        command = "python #{python_dir}/memo.py #{user_name} #{option}"
        @exec = require('child_process').exec
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    # News 
    robot.respond /news/i, (msg) ->
        command = "python #{python_dir}/news.py"
        @exec = require('child_process').exec
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    # Multi task
    robot.respond /multi/i, (msg) ->
        command_weather = "python #{python_dir}/weather.py 0"
        command_news = "python #{python_dir}/news.py"
        @exec = require('child_process').exec
        @exec command_weather, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?
        @exec command_news, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?

    # Gi-taka
    robot.hear /たかぎ|ぎーたか/i, (msg) ->
        command = "python #{python_dir}/random_comments.py takagi"
        @exec = require('child_process').exec
        @exec command, (error, stdout, stderr) ->
            msg.send error if error?
            msg.send stdout if stdout?
            msg.send stderr if stderr?
