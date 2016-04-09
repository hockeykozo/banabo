module.exports = (robot) ->
	robot.respond /dig (.*)/i, (msg) ->
		@exec = require('child_process').exec
		command = "bash /home/takashi/dev/banabo/scripts/sh/test.sh #{msg.match[1]}"
#		msg.send "Command: #{command}"
		@exec command, (error, stdout, stderr) ->
			msg.send error if error?
			msg.send stdout if stdout?
			msg.send stderr if stderr?
