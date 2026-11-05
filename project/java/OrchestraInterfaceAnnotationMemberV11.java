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
  One part of an annotation in an interfaces file, a text or a hint for software. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraInterfaceAnnotationMemberV11  {

  private OrchestraInterfaceDocumentationV11 fixiDocumentation;
  private OrchestraInterfaceAppinfoV11 fixiAppinfo;


}