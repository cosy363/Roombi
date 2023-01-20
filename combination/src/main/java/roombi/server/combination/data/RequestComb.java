package roombi.server.combination.data;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import java.util.Date;
import java.util.List;

@Data
@JsonInclude(JsonInclude.Include.NON_NULL)
public class RequestComb {

    @NotNull(message = "")
    private String userNumber;

    private List<Integer> furniturePreference;

    private List<Integer> colorPreference;

    private Integer budget;

}
