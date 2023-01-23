package roombi.server.user_service.dto;

import lombok.Data;
import roombi.server.user_service.data.ResponseHeartList;

import java.util.Date;
import java.util.List;

@Data
public class UserDto {
    private String userNumber;
    private String userId;
    private String pwd;

    private Date createdAt;

    private String encryptedPwd;

    private List<ResponseHeartList> heartLists;
}
