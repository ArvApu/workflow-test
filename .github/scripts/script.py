import argparse

def getAvailableServices() -> list[str]:
    return [
        'webservices',
        'backoffice',
        'backofficeapi',
        'queue-worker',
    ]

def getAvailableLambdas() -> list[str]:
    return [
        'sie4',
        'ssp',
        'gbat10',
        'xero',
        'garbageCollector',
        'exchangeRateUpdater',
        'automaticImport',
    ]

def run(args: argparse.Namespace) -> None:
    for service in args.services.split(','):
        if service not in getAvailableServices():
            raise Exception(f'Service {service} is not valid')

    for lambdaFunction in args.lambdas.split(','):
        if lambdaFunction not in getAvailableLambdas():
            raise Exception(f'Service {lambdaFunction} is not valid')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('services')
    parser.add_argument('lambdas')

    run(parser.parse_args())
