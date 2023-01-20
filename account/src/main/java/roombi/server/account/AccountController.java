package roombi.server.account;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("/account/")
public class AccountController {

    @GetMapping("/welcome")
    public String welcome() {
        return "Welcome to Account Maeddugi World";
    }

    @GetMapping("/print")
    public String print(@RequestHeader("account-header") String header) {
        log.info(header);
        return header;
    }
}
