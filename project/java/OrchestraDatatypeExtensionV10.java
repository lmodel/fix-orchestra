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
  XML from the target standard's own schema that a datatype mapping carries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraDatatypeExtensionV10  {

  private List<OrchestraXmlElement> fixrAny;


}