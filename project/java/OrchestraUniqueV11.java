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
  A check that a field's value is unique among the values that share the other fields it names, or among all values when it names none.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraUniqueV11  {

  private List<OrchestraFieldRefV11> fixrFieldRef;


}