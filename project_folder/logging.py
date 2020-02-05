CONFIG_DEFAULTS = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "hypercorn.error": {
            "level": "INFO",
            "handlers": ["error_console"],
            "propagate": True,
            "qualname": "hypercorn.error",
        },
        "hypercorn.access": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": True,
            "qualname": "hypercorn.access",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": "ext://sys.stdout",
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": "ext://sys.stderr",
        },
    },
    "formatters": {
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        }
    },
}

def _create_logger(
    name: str, target: Union[logging.Logger, str, None], level: str, sys_default: Any
) -> logging.Logger:
    if isinstance(target, logging.Logger):
        return target
    elif target is not None:
        logger = logging.getLogger(name)
        logger.propagate = False
        logger.handlers = []
        if target == "-":
            logger.addHandler(logging.StreamHandler(sys_default))
        else:
            logger.addHandler(logging.FileHandler(target))
        logger.setLevel(logging.getLevelName(level.upper()))
        return logger
    else:
        return None
