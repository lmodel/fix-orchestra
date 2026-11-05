package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A value, with what kind it is, that picks out a session, such as a sender or target ID.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraSessionIdentifierV11  {

  private String fixiText;
  private String fixiName;


}