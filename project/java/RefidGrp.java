package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A reference to a message element by its key identifiers
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RefidGrp  {

  private String scenarioId;
  private String id;
  private String name;
  private String scenario;


}