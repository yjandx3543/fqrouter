import dns_service
import tcp_service
import main


if '__main__' == __name__:
    main.setup_logging()
    dns_service.clean()
    tcp_service.clean()
