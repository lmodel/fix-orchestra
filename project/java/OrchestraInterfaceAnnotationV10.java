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
  Notes for readers and hints for software, attached to an element of an interfaces file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraInterfaceAnnotationV10  {

  private List<OrchestraInterfaceAnnotationMemberV10> fixiMembers;


}