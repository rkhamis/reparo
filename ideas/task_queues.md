# tasks queues

## typical task queues

- usually a combo of lpush, brpoplpush operations on two queues.


## investigate using lua
investigate using lua (builtin redis) to achieve reliability  http://oldblog.antirez.com/post/250

## use streams
https://redis.io/topics/streams-intro
as of Redis 5 there's support for stream data strucutre allowing 

- reliably handling the failure of worker to process a job
- no two workers get the same job a client received before
- no job is consumed until the worker `ack`s
- provides blocking/nonblocking apis
- allows to continue from beginning or the last received message
- easily achieves prioritization so we can have high prio and low prio streams.
