from collections import namedtuple

# https://gist.github.com/tsohr/5711945

ActivityFlagsTuple = namedtuple("ActivityFlags", [
    "ENABLE_DEBUGGING",
    "WAIT_COMPLETE_LAUNCH",
    "START_PROFILER",
    "PROFILER",
    "REPEAT",
    "STOP",
    "OPENGL_TRACE"
])

ActivityFlags = ActivityFlagsTuple(
    "D", "W", "-start-profiler", "P", "R", "S", "-opengl-trace:"
)
