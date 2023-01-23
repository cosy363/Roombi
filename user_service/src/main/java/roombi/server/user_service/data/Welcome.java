package roombi.server.user_service.data;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
@lombok.Data
//@AllArgsConstructor
//@NoArgsConstructor
public class Welcome {
    @Value("${welcome.secondmessage}")
    private String message;
}
